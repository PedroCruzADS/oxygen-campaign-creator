from datetime import datetime


def create_adset_model(adset_name: str, campaign_id: str, genders: list, age_min: int, age_max: int,
                       start_time: datetime, feed_face: list, feed_insta: list, pixel_id: str):

    return {'name': adset_name,
            'campaign_id': campaign_id,
            'billing_event': 'IMPRESSIONS',
            'promoted_object': {'pixel_id': pixel_id,
                                'custom_event_type': 'PURCHASE'},
            'targeting': {"geo_locations": {
                "countries": ['BR']},
                "custom_audiences": [],
                "excluded_custom_audiences": [],
                "genders": genders,
                "age_min": age_min,
                "age_max": age_max,
                'publisher_platforms': ['facebook', 'instagram'],
                "facebook_positions": feed_face,
                "instagram_positions": feed_insta,
                "flexible_spec": []
            },
            'start_time': start_time
            }
