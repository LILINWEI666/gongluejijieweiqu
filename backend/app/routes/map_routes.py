"""
地图 API 路由
"""
from flask import request, jsonify
from app.models import Attraction, Restaurant, PhotoSpot
from . import map_bp


@map_bp.route('/attractions', methods=['GET'])
def get_map_attractions():
    """获取地图上的景点"""
    city = request.args.get('city')
    
    query = Attraction.query
    if city:
        query = query.filter_by(city=city)
    
    attractions = query.all()
    
    data = []
    for attr in attractions:
        data.append({
            'id': attr.id,
            'name': attr.name,
            'latitude': attr.latitude,
            'longitude': attr.longitude,
            'type': 'attraction',
            'rating': attr.rating,
            'cover_image': attr.cover_image
        })
    
    return jsonify({'code': 0, 'message': 'success', 'data': data})


@map_bp.route('/restaurants', methods=['GET'])
def get_map_restaurants():
    """获取地图上的餐厅"""
    city = request.args.get('city')
    
    query = Restaurant.query
    if city:
        query = query.filter_by(city=city)
    
    restaurants = query.all()
    
    data = []
    for rest in restaurants:
        data.append({
            'id': rest.id,
            'name': rest.name,
            'latitude': rest.latitude,
            'longitude': rest.longitude,
            'type': 'restaurant',
            'rating': rest.rating,
            'cuisine_type': rest.cuisine_type,
            'cover_image': rest.cover_image
        })
    
    return jsonify({'code': 0, 'message': 'success', 'data': data})


@map_bp.route('/photo-spots', methods=['GET'])
def get_map_photo_spots():
    """获取地图上的打卡机位"""
    attraction_id = request.args.get('attraction_id')
    
    query = PhotoSpot.query
    if attraction_id:
        query = query.filter_by(attraction_id=attraction_id)
    
    spots = query.all()
    
    data = []
    for spot in spots:
        data.append({
            'id': spot.id,
            'name': spot.name,
            'latitude': spot.latitude,
            'longitude': spot.longitude,
            'type': 'photo_spot',
            'attraction_id': spot.attraction_id,
            'rating': spot.rating,
            'cover_photo': spot.cover_photo
        })
    
    return jsonify({'code': 0, 'message': 'success', 'data': data})


@map_bp.route('/all', methods=['GET'])
def get_map_all():
    """获取地图上的所有标记点"""
    city = request.args.get('city')
    
    data = []
    
    attractions = Attraction.query.filter_by(city=city).all() if city else Attraction.query.all()
    for attr in attractions:
        data.append({
            'id': attr.id,
            'name': attr.name,
            'latitude': attr.latitude,
            'longitude': attr.longitude,
            'type': 'attraction',
            'rating': attr.rating,
            'cover_image': attr.cover_image
        })
    
    restaurants = Restaurant.query.filter_by(city=city).all() if city else Restaurant.query.all()
    for rest in restaurants:
        data.append({
            'id': rest.id,
            'name': rest.name,
            'latitude': rest.latitude,
            'longitude': rest.longitude,
            'type': 'restaurant',
            'rating': rest.rating,
            'cuisine_type': rest.cuisine_type,
            'cover_image': rest.cover_image
        })
    
    return jsonify({'code': 0, 'message': 'success', 'data': data})
