<template>
  <main class="container">
    <div class="row mb-2 m-4">

      <div class="col-md-10">
        <div class="row g-0 rounded overflow-hidden flex-md-row mb-4 h-md-250 position-relative">

          <div class="col-auto d-none d-lg-block">
            <img :src="photo_path" class="bd-placeholder-img card-img-top" role="img" aria-label="Photo: Photo" width="420" />
          </div>

          <div class="col p-4 d-flex flex-column position-static">
            <h3 class="mb-0">{{type}}</h3>
            <div class="mb-1 text-muted">#{{registration_number}}</div>
            широта: {{x_coord}}<br />
            долгота: {{y_coord}}<br />
            радиус кроны: {{crown_radius}}<br />
            возраст (годы): {{age}}<br />
            состояние: {{condition}}<br />
            необходимые работы: {{list_tasks}}
          </div>

        </div>
      </div>

    </div>
  </main>
</template>

<script>
export default {
  name: "DetailTreeView",
  data() {
    return {
      pk: null,
      registration_number: null,
      x_coord: null,
      y_coord: null,
      crown_radius: null,
      age: null,
      type: null,
      condition: null,
      photo_path: null,
      list_tasks: null,
    }
  },
  async mounted() {
    await this.fetchTrees()
  },
  methods: {
    async fetchTrees(url) {
      const targetUrl = url ? url : `/api/${this.$route.params.id}`;
      const res = await fetch(targetUrl);
      const data = await res.json();
      this.pk = data["pk"];
      this.registration_number = data["registration_number"];
      this.x_coord = data["x_coord"];
      this.y_coord = data["y_coord"];
      this.crown_radius = data["crown_radius"];
      this.age = data["age"];
      this.type = data["type"];
      this.condition = data["condition"];
      this.photo_path = data["photo_path"];
      this.list_tasks = data["list_tasks"];
    },
  }
}
</script>

<style scoped>
.col-md-10 {
  border: solid 2px #212529;
  border-radius: 5px;
  box-shadow: 4px 4px 10px #5e5e5e;
}
</style>