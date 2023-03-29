from classes.segmentations import Segmentations
from facebook_business.adobjects.adset import AdSet

from classes.segmentations_id import SegmentationsId


def check_adset(adset: AdSet, segmentation: str, broad_regions: list, interests: list, is_dynamic_adset: bool):
    seg = Segmentations()
    seg_id = SegmentationsId()

    if segmentation == seg.lookalike:
        adset["targeting"]["custom_audiences"] = [
            seg_id.lookalike_1,
            seg_id.lookalike_2,
            seg_id.lookalike_3,
            seg_id.lookalike_4]
        adset["targeting"]["age_min"] = 18
        adset["targeting"]["age_max"] = 65
        adset["targeting"]["excluded_custom_audiences"] = [
            seg_id.purchase_30d]
        adset['is_dynamic_creative'] = is_dynamic_adset
        return adset

    if segmentation == seg.add_cart:
        adset["targeting"]["custom_audiences"] = [
            seg_id.add_cart, seg_id.cart]
        adset["targeting"]["excluded_custom_audiences"] = [
            seg_id.purchase_30d]
        adset["targeting"]["age_min"] = 18
        adset["targeting"]["age_max"] = 65
        adset['is_dynamic_creative'] = is_dynamic_adset

        return adset

    if segmentation == seg.view_content:
        adset["targeting"]["custom_audiences"] = [
            seg_id.view_content, seg_id.email]
        adset["targeting"]["excluded_custom_audiences"] = [
            seg_id.purchase_30d]
        adset["targeting"]["age_min"] = 18
        adset["targeting"]["age_max"] = 65
        adset['is_dynamic_creative'] = is_dynamic_adset

        return adset

    if segmentation == seg.purchase180d:
        adset["targeting"]["custom_audiences"] = [
            seg_id.purchase_180d]
        adset["targeting"]["excluded_custom_audiences"] = [
            seg_id.purchase_30d]
        adset["targeting"]["age_min"] = 18
        adset["targeting"]["age_max"] = 65
        adset['is_dynamic_creative'] = is_dynamic_adset

        return adset

    if segmentation == seg.broad:
        adset["targeting"]["excluded_custom_audiences"] = [
            seg_id.purchase_30d]
        del adset['targeting']['geo_locations']['countries']
        adset["targeting"]["geo_locations"]['regions'] = [
            x for xs in broad_regions for x in xs]
        adset["targeting"]["flexible_spec"] = [{
            "interests": interests},
            {
            "behaviors": [{
                "id": "6071631541183",
                "name": "Compradores envolvidos"
            }]
        }
        ]
        adset['is_dynamic_creative'] = is_dynamic_adset
        return adset
