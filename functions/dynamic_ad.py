from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adaccount import AdAccount


def create_dynamic_ads(text_list: str, title_list: str, adset_id_list: list, ad_account_id: str, campaign_name: str, page_id: str,
                       instagram_actor_id: str, img_files: list, call_to_action: str, link: str, status: str, pixel_id: str):

    for adset_id in adset_id_list:
        adset_name = AdSet(adset_id).remote_read(
            fields=[AdSet.Field.name])
        adset_name = adset_name['name'].lower()
        adcreative = AdAccount(ad_account_id).create_ad_creative(
            fields=[],
            params={
                "asset_feed_spec": {
                    "ad_formats": [
                        "AUTOMATIC_FORMAT"
                    ],
                    "bodies": [
                        {
                            "text": text_list[0]
                        },
                        {
                            "text": text_list[1]
                        }
                    ],
                    "call_to_action_types": [
                        call_to_action
                    ],
                    "images": [
                        {
                            "hash": img_files[0]
                        },
                        {
                            "hash": img_files[1]
                        }
                    ],
                    "link_urls": [
                        {
                            "website_url": link
                        }
                    ],
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
                'url_tags': f'?utm_source=facebook&utm_medium=cpc&utm_campaign={campaign_name}_{adset_name}&utm_content=anuncio_{adset_id}',
                'object_story_spec': {'page_id': page_id,
                                      'instagram_actor_id': instagram_actor_id,
                                      }},
        )

        params = {
            'name': f'anuncio_{adset_id}',
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


def create_story_ads(adset_id, ad_account_id, call_to_action, img_files, link, campaign_name,
                     page_id, instagram_actor_id, status, pixel_id):

    adset_name = AdSet(adset_id).api_get(
        fields=[AdSet.Field.name])
    adset_name = adset_name['name'].lower()
    adcreative = AdAccount(ad_account_id).create_ad_creative(
        fields=[],
        params={
            "asset_feed_spec": {
                "ad_formats": [
                    "AUTOMATIC_FORMAT"
                ],
                "call_to_action_types": [
                    call_to_action
                ],
                "images": [
                    {
                        "hash": img_files[0]
                    },
                    {
                        "hash": img_files[1]
                    }
                ],
                "link_urls": [
                    {
                        "website_url": link
                    }
                ],
            },
            'name': f'anuncio_{adset_id}',
            'url_tags': f'?utm_source=facebook&utm_medium=cpc&utm_campaign={campaign_name}_{adset_name}&utm_content=anuncio_{adset_id}',
            'object_story_spec': {'page_id': page_id,
                                  'instagram_actor_id': instagram_actor_id,
                                  }},
    )

    params = {
        'name': f'anuncio_{adset_id}',
        'adset_id': adset_id,
        'creative': {'creative_id': adcreative['id']},
        'status': status,
        "conversion_domain": "oscarcalcados.com.br",
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
