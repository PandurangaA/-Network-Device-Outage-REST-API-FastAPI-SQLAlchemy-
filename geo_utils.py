def to_geojson(devices):
    features = []
    for d in devices:
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [d.longitude, d.latitude]},
            "properties": {"id": d.id, "name": d.name, "type": d.type}
        })
    return {"type": "FeatureCollection", "features": features}
