<template>

  <div class="d-flex justify-content-center m-3">
    <div id="mapContainer"></div>
  </div>

</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";

export default {
  name: "HomeView",
  data() {
    return {
      trees: [],
      map: null
    }
  },
  async mounted() {
    await this.fetchTrees();
    this.map = L.map("mapContainer").setView([49.23317838692403, 28.4664426529637], 18);
    await this.drawCircleOnMap();
    L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.map);
  },
  methods: {
    async fetchTrees(url) {
        let targetUrl = url ? url : '/api/';
        let res = await fetch(targetUrl);
        let data = await res.json();
        this.trees = data["results"];
      while(data["next_link"] != null) {
        targetUrl = data["next_link"];
        res = await fetch(targetUrl);
        data = await res.json();
        this.trees = this.trees.concat(data["results"]);
      }
    },
    async drawCircleOnMap() {
      for (const tree of this.trees) {
        L.circle([tree.x_coord, tree.y_coord], {radius: tree.crown_radius, color: 'LimeGreen'}).addTo(this.map);
      }
    },
  }
}
</script>

<style scoped>
#mapContainer {
  width: 1280px;
  height: 768px;
  border: solid 2px #212529;
  border-radius: 5px;
  box-shadow: 8px 8px 15px #212529;
}
</style>
