/**
 * Created by Conner on 6/28/2017.
 */
// var mapData;

function getDataOne(){
    $.ajax({
        dataType: 'json',
        url: "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson",
        data: {

        },
        success: function (data) {
            console.log(data);
    //, new ol.layer.Tile({source: new ol.source.OSM()})

         var count = data.features.length;
         console.log(data.features[0].properties['mag']);
      var features = new Array(count);
      // console.log(data.features[0].geometry['coordinates']);
      var e = 18000000;
      for (var i = 0; i < count; ++i) {
        features[i] = new ol.Feature({
          'geometry': new ol.geom.Point(
              ol.proj.fromLonLat([data.features[i].geometry['coordinates'][0], data.features[i].geometry['coordinates'][1]])),
          'i': i,
          'size': data.features[i].properties['mag'] > 0 ? data.features[i].properties['mag'] : 0.01
        });
      }

      function styles(size) {
        return new ol.style.Style({
          image: new ol.style.Circle({
            radius: size * 2,
            fill: new ol.style.Fill({color: '#666666'}),
            stroke: new ol.style.Stroke({color: '#bada55', width: 1})
          })
        })
      }

      var vectorSource = new ol.source.Vector({
        features: features,
        wrapX: false
      });
      var vector = new ol.layer.Vector({
        source: vectorSource,
        style: function(feature) {
          return styles(feature.get('size'));
        }
      });

      var map = new ol.Map({
        layers: [new ol.layer.Tile({source: new ol.source.OSM()}), vector],
        target: document.getElementById('map'),
        view: new ol.View({
          center: [0, 0],
          zoom: 2
        })
      });

      // var point = null;
      // var line = null;
      // var displaySnap = function(coordinate) {
      //   var closestFeature = vectorSource.getClosestFeatureToCoordinate(coordinate);
      //   if (closestFeature === null) {
      //     point = null;
      //     line = null;
      //   } else {
      //     var geometry = closestFeature.getGeometry();
      //     var closestPoint = geometry.getClosestPoint(coordinate);
      //     if (point === null) {
      //       point = new ol.geom.Point(closestPoint);
      //     } else {
      //       point.setCoordinates(closestPoint);
      //     }
      //     if (line === null) {
      //       line = new ol.geom.LineString([coordinate, closestPoint]);
      //     } else {
      //       line.setCoordinates([coordinate, closestPoint]);
      //     }
      //   }
      //   map.render();
      // };
      //
      // map.on('pointermove', function(evt) {
      //   if (evt.dragging) {
      //     return;
      //   }
      //   var coordinate = map.getEventCoordinate(evt.originalEvent);
      //   displaySnap(coordinate);
      // });
      //
      // map.on('click', function(evt) {
      //   displaySnap(evt.coordinate);
      // });
      //
      // var stroke = new ol.style.Stroke({
      //   color: 'rgba(255,255,0,0.9)',
      //   width: 3
      // });
      // var style = new ol.style.Style({
      //   stroke: stroke,
      //   image: new ol.style.Circle({
      //     radius: 10,
      //     stroke: stroke
      //   })
      // });
      //
      // map.on('postcompose', function(evt) {
      //   var vectorContext = evt.vectorContext;
      //   vectorContext.setStyle(style);
      //   if (point !== null) {
      //     vectorContext.drawGeometry(point);
      //   }
      //   if (line !== null) {
      //     vectorContext.drawGeometry(line);
      //   }
      // });
      //
      // map.on('pointermove', function(evt) {
      //   if (evt.dragging) {
      //     return;
      //   }
      //   var pixel = map.getEventPixel(evt.originalEvent);
      //   var hit = map.hasFeatureAtPixel(pixel);
      //   if (hit) {
      //     map.getTarget().style.cursor = 'pointer';
      //   } else {
      //     map.getTarget().style.cursor = '';
      //   }
      // });



      }
    });

}

getDataOne();