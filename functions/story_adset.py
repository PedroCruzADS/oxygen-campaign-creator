from datetime import datetime
from classes.segmentations_id import SegmentationsId
from classes.positions import Position


def create_story_adset(adset_name: str, campaign_id: str, genders: list, age_min: int, age_max: int,
                       start_time: datetime, pixel_id: str):

    return {'name': adset_name,
            'campaign_id': campaign_id,
            'billing_event': 'IMPRESSIONS',
            'promoted_object': {'pixel_id': pixel_id,
                                'custom_event_type': 'PURCHASE'},
            'targeting': {"geo_locations": {
                "countries": ['BR']},
                "custom_audiences": SegmentationsId().all_segs_id,
                "excluded_custom_audiences": SegmentationsId().purchase_30d,
                "genders": genders,
                "age_min": age_min,
                "age_max": age_max,
                'publisher_platforms': ['facebook', 'instagram'],
                "facebook_positions": Position().facebook_stories,
                "instagram_positions": Position().insta_stories,
                "flexible_spec": [],
            },
            'start_time': start_time,
            'is_dynamic_creative': 'true'
            }
