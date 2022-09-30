$(function () {
  function getColor(d) {
    if (!d) return "gray";
    return d > 13000
      ? "#ff0000"
      : d > 12000
      ? "#cc3300"
      : d > 11000
      ? "#e76832"
      : d > 10000
      ? "#e7961a"
      : d > 9000
      ? "#ffae00"
      : d > 8500
      ? "#ffff33"
      : d > 8000
      ? "#d7f221"
      : d > 7500
      ? "#abd74c"
      : d > 7000
      ? "#708f03"
      : "#486900";
  }

  function style(feature) {
    return {
      fillColor: getColor(feature.properties.price),
      weight: 1.5,
      opacity: 1,
      color: "lightgrey",
      fillOpacity: 0.7,
    };
  }

  var View = {
    map: null,

    initMap: function () {
      View.map = L.map("map");
      var osmLayer = L.tileLayer(
        "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        {}
      );
      View.map.setView(new L.LatLng(48.8586895, 2.3401934), 12);
      View.map.addLayer(osmLayer);
      $("#progress").show();
      View.loadGeoms();
    },

    loadGeoms: function () {
      $.getJSON("/api/geoms", function (geojsonFeature) {
        L.geoJson(geojsonFeature, {
          style: style,
          onEachFeature: function (feature, layer) {
            layer.on("click", function (e) {
              View.clickGeom(feature);
            });
          },
        }).addTo(View.map);
        $("#progress").hide();
      });
    },

    clickGeom: function (feature) {
      var cog = feature.properties.cog;
      var url = "/api/get_price/" + cog;
      $.getJSON(url, function (data) {
        $("#progress").show();
        View.updateChart(data.volumes, data.labels, data.serie_name);
        $("#progress").hide();
      });
    },

    updateChart: function (volumes, labels, serie_name) {
      $("#chart").highcharts({
        chart: {
          type: "column",
        },
        title: {
          text: "Distribution des prix",
        },
        xAxis: {
          categories: labels,
        },
        yAxis: {
          min: 0,
          title: {
            text: "Volumes",
          },
        },
        plotOptions: {
          column: {
            pointPadding: 0.2,
            borderWidth: 0,
          },
        },
        series: [
          {
            name: serie_name,
            data: volumes,
          },
        ],
      });
    },
  };

  View.initMap();
});
