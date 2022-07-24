<template>
  <div class="m-3">

    <!-- pagination -->
    <nav>
      <ul class="pagination justify-content-center">

        <li class="page-item" v-if="previous_link">
          <a class="page-link" @click="fetchTrees(previous_link)">&laquo;</a>
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link" href="#">&laquo;</a>
        </li>

        <li class="page-item" v-if="previous_link">
          <a class="page-link" @click="fetchTrees(previous_link)">{{previous_number}}</a>
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link" href="#">{{current_number-1}}</a>
        </li>

        <li class="page-item active" aria-current="page">
          <span class="page-link">{{current_number}}</span>
        </li>

        <li class="page-item" v-if="next_link">
          <a class="page-link" @click="fetchTrees(next_link)">{{next_number}}</a>
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link" href="#">{{current_number+1}}</a>
        </li>

        <li class="page-item" v-if="next_link">
          <a class="page-link" @click="fetchTrees(next_link)">&raquo;</a>
        </li>
        <li class="page-item disabled" v-else>
          <a class="page-link" href="#">&raquo;</a>
        </li>

      </ul>
    </nav>

    <!-- list trees -->
    <div class="album py-1 bg-white">
        <div class="container">
          <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

            <div class="col" v-for="tree in trees">
              <a :href="'/tree_detail/' + tree.pk" class="link-no-decor">
                <div class="card">
                  <img :src="tree.photo_path" class="bd-placeholder-img card-img-top" role="img" aria-label="Photo: Photo" />
                  <div class="card-body">
                    <p class="card-text"><b>{{tree.type}}</b></p>
                    <p class="card-text">#{{tree.registration_number}}</p>
                  </div>
                </div>
              </a>
            </div>

          </div>
        </div>
      </div>

  </div>
</template>

<script>
export default {
  name: "ListTrees",
  data() {
    return {
      trees: [],
      previous_link: null,
      previous_number: null,
      current_number: null,
      next_number: null,
      next_link: null,
    }
  },
  async mounted() {
    await this.fetchTrees()
  },
  methods: {
    async fetchTrees(url) {
      const targetUrl = url ? url : '/api/';
      const res = await fetch(targetUrl);
      const data = await res.json();
      this.trees = data["results"];
      this.previous_link = data["previous_link"];
      this.previous_number = data["previous_number"];
      this.current_number = data["current_number"];
      this.next_number = data["next_number"];
      this.next_link = data["next_link"];
    },
  }
}
</script>

<style scoped>
.card {
  border: solid 2px #212529;
  border-radius: 5px;
  box-shadow: 4px 4px 10px #5e5e5e;
}
.card-body {
  background-color: lightgrey;
}
</style>
