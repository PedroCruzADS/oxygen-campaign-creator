from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adaccount import AdAccount


def create_ads(text_list: str, title_list: str, adset_id_list: list, ad_account_id: str, campaign_name: str, page_id: str,
               instagram_actor_id: str, img_files: list, call_to_action: str, link: str, status: str, pixel_id: str):

    for titulo in range(len(title_list)):
        for adset_id in adset_id_list:
            adset_name = AdSet(adset_id).remote_read(
                fields=[AdSet.Field.name])
            adset_name = adset_name['name'].lower()
            adcreative = AdAccount(ad_account_id).create_ad_creative(
                fields=[],
                params={
                    "asset_feed_spec": {
                        "bodies": [
                            {
                                "text": text_list[0]
                            },
                            {
                                "text": text_list[1]
                            }
                        ],
                        "optimization_type": "DEGREES_OF_FREEDOM",
                        "titles": [
                            {
                                "text": title_list[0]
                            },
                            {
                                "text": title_list[1]
                            }
                        ]
                    },
                    'name': title_list[0],
                    'url_tags': f'?utm_source=facebook&utm_medium=cpc&utm_campaign={campaign_name}_{adset_name}&utm_content=anuncio_{titulo + 1}',
                    'object_story_spec': {'page_id': page_id,
                                          'instagram_actor_id': instagram_actor_id,
                                          'link_data': {'image_hash': img_files[titulo],
                                                        "call_to_action": {"type": call_to_action},
                                                        'link': link}}},
            )

            params = {
                'name': f'anuncio_{titulo+1}',
                'adset_id': adset_id,
                'creative': {'creative_id': adcreative['id']},
                'status': status,
                "conversion_domain": "",
                "tracking_specs":
                [{
                    "action.type": [
                        "offsite_conversion"
                    ],
                    "fb_pixel": [
                        pixel_id
                    ]
                }],

            }

            AdAccount(ad_account_id).create_ad(
                fields=[],
                params=params)
