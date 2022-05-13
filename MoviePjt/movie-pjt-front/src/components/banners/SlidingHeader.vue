<template>
  <header
    class="sliding-header"
    :class="{
      header: scrollY < median,
      /// 'hidden': scrollY > thresholdHide && scrollY < thresholdOpen
    }"
  >
    <slot name="header" v-if="scrollY < median"></slot>
  </header>
</template>

<script>
export default {
  name: "SlidingHeader",
  data() {
    return {
      scrollY: 0,
    };
  },
  props: {
    thresholdHide: Number,
    thresholdOpen: Number,
  },
  computed: {
    median() {
      return (this.thresholdHide + this.thresholdOpen) / 2;
    },
  },
  created() {
    window.addEventListener("scroll", () => {
      this.scrollY = window.scrollY;
    });
  },
};
</script>

<style>
.sliding-header {
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  width: 100%;
  transition: 0.3s;
}
</style>
