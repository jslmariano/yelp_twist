<template>
  <div class="home">
    <button @click="$router.push('/new')">Add Order</button>
    <hr />
    <div class="container">
      <div class="order" v-for="order in orders" :key="order.user_id" :order="order">
        <p>
          <em>"{{order.name}}"</em>
          by {{order.name}}
        </p>

        <span class="added-by">added by {{order.name}}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data: () => ({
    orders: []
  }),
  created() {
    fetch("http://localhost/api/v1/customer/")
      .then(res => res.json())
      .then(response => {
        this.orders = response.orders;
      })
      .catch(e => {
        console.error(e.message);
      });
  }
};
</script>


<style  scoped>
.home {
  width: 100%;
}

button {
  cursor: pointer;
  border: 1px solid steelblue;
  border-radius: 5px;
  background: white;
  color: steelblue;
  height: 2em;
}

button:hover {
  background: steelblue;
  color: white;
}

.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.order {
  width: 29%;
  padding: 0.5rem;
  margin: 1%;
  border-radius: 10px;
  border: 1px solid steelblue;
  color: black;
}

.order span.by {
  text-decoration: underline;
}

.order .added-by {
  color: rgba(0, 0, 0, 0.6);
  margin-top: 3em;
}
</style>