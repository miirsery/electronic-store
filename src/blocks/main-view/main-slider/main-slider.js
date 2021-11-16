import SwiperCore, { Pagination, Navigation, Autoplay, EffectCoverflow } from 'swiper/core';
// import Swiper from "swiper";
SwiperCore.use([Pagination, Navigation, Autoplay, EffectCoverflow])
var swiper = new SwiperCore(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    observeParents: true,
    observer: true,
    pagination: {
        el: ".swiper-pagination",
        type: 'bullets',
        clickable: true,
        dynamicBullets: true
    },

    autoplay: {
        delay: 1500,
    },
    speed: 800,

    effect: 'coverflow',
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 10,
        modifier: 2,
        slideShadows: true,
    },
    breakpoints: {
        1230: {
            slidesPerView: 2.85,
            spaceBetween: 30,
        },
        1180: {
            slidesPerView: 2.85,
            spaceBetween: 10,
        },
        1000: {
            slidesPerView: 2.73,
            spaceBetween: 5,
        },
        450: {
            slidesPerView: 1.7,
            spaceBetween: -90,
        },
        380: {
            slidesPerView: 1.3,
            spaceBetween: -100,
        }
    },
});

