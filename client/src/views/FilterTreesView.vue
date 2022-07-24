<template>

  <div class="album py-3 bg-white">
    <div class="container">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

        <!-- left radio -->
        <div class="filter left">
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefaultL" id="flexRadioDefault1" checked v-on:click="radio($event)">
            <label class="form-check-label" for="flexRadioDefault1">
              все
            </label>
          </div>

          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefaultL" id="flexRadioDefault2" v-on:click="radio($event)">
            <label class="form-check-label" for="flexRadioDefault2">
              менее &lt; 10 лет
            </label>
          </div>

          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefaultL" id="flexRadioDefault3" v-on:click="radio($event)">
            <label class="form-check-label" for="flexRadioDefault3">
              более &gt; 10 лет
            </label>
          </div>
        </div>

        <!-- middle radio -->
        <div class="filter none">
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefaultN" id="flexRadioDefault4" checked v-on:click="radio($event)">
            <label class="form-check-label" for="flexRadioDefault4">
              все
            </label>
          </div>

          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefaultN" id="flexRadioDefault5" v-on:click="radio($event)">
            <label class="form-check-label" for="flexRadioDefault5">
              радиус кроны менее &lt; 4м.
            </label>
          </div>

          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefaultN" id="flexRadioDefault6" v-on:click="radio($event)">
            <label class="form-check-label" for="flexRadioDefault6">
              радиус кроны более &gt; 4м.
            </label>
          </div>
        </div>

        <!-- right radio -->
        <div class="filter right">
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefaultR" id="flexRadioDefault7" checked v-on:click="radio($event)">
            <label class="form-check-label" for="flexRadioDefault7">
              все
            </label>
          </div>

          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefaultR" id="flexRadioDefault8" v-on:click="radio($event)">
            <label class="form-check-label" for="flexRadioDefault8">
              ЕСТЬ необходимые работы
            </label>
          </div>

          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefaultR" id="flexRadioDefault9" v-on:click="radio($event)">
            <label class="form-check-label" for="flexRadioDefault9">
              НЕТ необходимых работ
            </label>
          </div>
        </div>

        <div class="card" style="width: 18rem;" v-for="tree in filter_trees">
          <a :href="'/tree_detail/' + tree.pk" class="link-no-decor">
            <div class="card-body">
              <h5 class="card-title">{{tree.type}}</h5>
              <p class="card-text">#{{tree.registration_number}}</p>
            </div>
          </a>
        </div>

      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "FilterTreeView",
  data() {
    return {
      trees: [],
      filter_trees: [],
      age: 1,    // 1, 2, 3
      radius: 4, // 4, 5, 6
      tasks: 7,  // 7, 8 ,9
    }
  },
  async mounted() {
    await this.fetchTrees();
  },
  methods: {
    // doFilter() {
    //   if (this.age === 1 && this.radius === 1 && this.tasks === 1) {
    //     this.filter_trees = this.trees;
    //   }
    //   // else if ()
    //   //   statement2
    //   // else if ()
    //   //
    //   // else
    //   //
    //   this.$forceUpdate()
    // },
    radio: function (event) {
      const targetId = parseInt(event.currentTarget.id.slice(-1));
      switch (targetId) {
        case 1:
        case 2:
        case 3:
          this.age = targetId;
          break;
        case 4:
        case 5:
        case 6:
          this.radius = targetId;
          break;
        case 7:
        case 8:
        case 9:
          this.tasks = targetId;
          break;
      }
      this.filter_trees = this.trees;
      if (this.age === 2) {
        //
      }
      else { // 3
        //
      }
      if (this.radius === 5) {
        //
      }
      else { // 6
        //
      }
      if (this.tasks === 8) {
        //
      }
      else { // 9
        //
      }
    },
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
        this.filter_trees = this.trees
      }
    }
  }
}
</script>

<style scoped>
.filter.left {
  float: left;
}
.filter.right {
  float: right;
}
.filter.none {
  float: none;
  margin-bottom: 10px;
}
.card {
  margin: 2px;
}
</style>