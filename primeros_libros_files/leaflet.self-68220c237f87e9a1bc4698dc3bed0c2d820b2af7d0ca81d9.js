




L.Icon.Default = L.Icon.Default.extend({
  _getIconUrl: function (name) {
    var paths = {"icon-2x.png":"/assets/marker-icon-2x-00179c4c1ee830d3a108412ae0d294f55776cfeb085c60129a39aa6fc4ae2528.png","shadow.png":"/assets/marker-shadow-264f5c640339f042dd729062cfc04c17f8ea0f29882b538e3848ed8f10edb4da.png","icon.png":"/assets/marker-icon-574c3a5cca85f4114085b6841596d62f00d7c892c7b03f28cbfa301deb1dc437.png"};
    return paths[name + '.png'];
  },

  _detectIconPath: function () {
    return '';
  }
});
L.Marker = L.Marker.extend({
  options: {
    icon: new L.Icon.Default()
  }
});

L.marker = function(latlng, options) {
  return new L.Marker(latlng, options);
}

