import datetime
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi
from flask import request
from classes.interests import Interest
from functions.check_adset import check_adset
from classes.genders import Gender
from classes.positions import Position

from classes.regions import Region
from classes.segmentations import Segmentations
from functions.adset import create_adset_model
from functions.campaign import create_campaign_model
from functions.ad import create_ads
from functions.creative_images import create_hash_images
from functions.dynamic_ad import create_dynamic_ads, create_story_ads
from functions.story_adset import create_story_adset


def main(files_dst: str):

    FacebookAdsApi.init(access_token=request.form['access_token'])

    ad_account_id = 'act_' + request.form['ad_account_id']
    instagram_actor_id = request.form['instagram_actor_id']
    page_id = request.form['facebook_page_id']

    campaign_result = AdAccount(
        ad_account_id).create_campaign(params=create_campaign_model(name=request.form['campaign_name'], objective=request.form['objective'],
                                                                    status=request.form['status'], daily_budget=request.form['daily_budget']))

    today = datetime.date.today()
    start_time = str(today)

    segmentations = Segmentations()
    region = Region()
    gender = Gender()
    position = Position()
    interest = Interest()

    genders = [request.form[x]
               for x in gender.genders if x in request.form]

    regions = [region.region_keys[x]
               for x in region.region_keys if x in request.form]

    interests = [interest.interests[x]
                 for x in interest.interests if x in request.form]

    titulos = [request.form['titulo_1'], request.form['titulo_2']]
    descricoes = [request.form['descricao_1'], request.form['descricao_2']]

    if 'feed' in request.form:
        feed_face = position.facebook
        feed_insta = position.instagram
    else:
        feed_face = []
        feed_insta = []

    adset_ids = []
    for seg in segmentations.check_list:
        if seg in request.form:
            adset = AdSet(parent_id=ad_account_id)

            adset.update(create_adset_model(adset_name=request.form[seg], campaign_id=campaign_result['id'],
                         genders=genders, age_min=request.form['age_min'], start_time=start_time,
                         age_max=request.form['age_max'], feed_face=feed_face, feed_insta=feed_insta, pixel_id=request.form['pixel_id']))

            adset = check_adset(
                adset=adset, segmentation=seg, broad_regions=regions, interests=interests, is_dynamic_adset=request.form['is_dynamic_campaign'])

            adset.remote_create()

            adset_ids.append(adset['id'])

    if request.files:
        hash_files = create_hash_images(
            request.files, files_dst, ad_account_id=ad_account_id)

    campaign_name = request.form['campaign_name'].replace(' ', '_').lower()

    if 'story' in request.form:
        adset_story = AdSet(parent_id=ad_account_id)

        adset_story.update(create_story_adset(
            adset_name='Stories', campaign_id=campaign_result['id'], genders=genders, age_min=request.form['age_min'],
            age_max=request.form['age_max'], start_time=start_time, pixel_id=request.form['pixel_id']
        ))
        adset_story.remote_create()

        create_story_ads(adset_story['id'], ad_account_id=ad_account_id, call_to_action=request.form['call_to_action'],
                         img_files=[hash_files[2], hash_files[3]
                                    ], link=request.form['link'], campaign_name=campaign_name,
                         page_id=page_id, instagram_actor_id=instagram_actor_id, status=request.form['status'], pixel_id=request.form['pixel_id'])

    if request.form['is_dynamic_campaign'] == 'true':
        create_dynamic_ads(descricoes, titulos, adset_ids, ad_account_id,
                           campaign_name, page_id, instagram_actor_id, [
                               hash_files[0], hash_files[1]],
                           request.form['call_to_action'], request.form['link'],
                           request.form['status'], request.form['pixel_id'])
    else:
        create_ads(descricoes, titulos, adset_ids, ad_account_id,
                   campaign_name, page_id, instagram_actor_id, [
                       hash_files[0], hash_files[1]],
                   request.form['call_to_action'], request.form['link'],
                   request.form['status'], request.form['pixel_id'])
