
document.addEventListener("DOMContentLoaded", function () {


    /* =====================================================
       MOBILE NAVIGATION
    ===================================================== */

    const menuToggle =
        document.getElementById("mobileMenuToggle");

    const navbar =
        document.getElementById("navbar");


    if (menuToggle && navbar) {

        menuToggle.addEventListener("click", function () {

            navbar.classList.toggle("active");

            menuToggle.classList.toggle("active");


            const icon =
                menuToggle.querySelector("i");


            if (navbar.classList.contains("active")) {

                if (icon) {

                    icon.classList.remove("fa-bars");

                    icon.classList.add("fa-xmark");

                }

                menuToggle.setAttribute(
                    "aria-label",
                    "Close navigation"
                );

            } else {

                if (icon) {

                    icon.classList.remove("fa-xmark");

                    icon.classList.add("fa-bars");

                }

                menuToggle.setAttribute(
                    "aria-label",
                    "Open navigation"
                );

            }

        });


        /* Close mobile menu after clicking a link */

        const navLinks =
            navbar.querySelectorAll("a");


        navLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                navbar.classList.remove("active");

                menuToggle.classList.remove("active");


                const icon =
                    menuToggle.querySelector("i");


                if (icon) {

                    icon.classList.remove("fa-xmark");

                    icon.classList.add("fa-bars");

                }

                menuToggle.setAttribute(
                    "aria-label",
                    "Open navigation"
                );

            });

        });

    }



    /* =====================================================
       HEADER SCROLL EFFECT
    ===================================================== */

    const header =
        document.querySelector(".site-header");


    function updateHeader() {

        if (!header) {
            return;
        }


        if (window.scrollY > 30) {

            header.classList.add("scrolled");

        } else {

            header.classList.remove("scrolled");

        }

    }


    window.addEventListener(
        "scroll",
        updateHeader
    );


    updateHeader();



    /* =====================================================
       SCROLL REVEAL ANIMATION
    ===================================================== */

    const revealElements =
        document.querySelectorAll(".reveal");


    if ("IntersectionObserver" in window) {

        const observer =
            new IntersectionObserver(

                function (entries, observer) {

                    entries.forEach(function (entry) {

                        if (entry.isIntersecting) {

                            entry.target.classList.add(
                                "active"
                            );

                            observer.unobserve(
                                entry.target
                            );

                        }

                    });

                },

                {
                    threshold: 0.10
                }

            );


        revealElements.forEach(function (element) {

            observer.observe(element);

        });

    } else {

        revealElements.forEach(function (element) {

            element.classList.add("active");

        });

    }



    /* =====================================================
       SMOOTH SCROLL
    ===================================================== */

    const anchorLinks =
        document.querySelectorAll(
            'a[href^="#"]'
        );


    anchorLinks.forEach(function (link) {

        link.addEventListener(
            "click",
            function (event) {

                const targetId =
                    this.getAttribute("href");


                if (
                    !targetId ||
                    targetId === "#"
                ) {
                    return;
                }


                const target =
                    document.querySelector(
                        targetId
                    );


                if (target) {

                    event.preventDefault();


                    target.scrollIntoView({

                        behavior: "smooth",

                        block: "start"

                    });

                }

            }
        );

    });



    /* =====================================================
       CURRENT YEAR
    ===================================================== */

    const yearElement =
        document.querySelector(
            "[data-current-year]"
        );


    if (yearElement) {

        yearElement.textContent =
            new Date().getFullYear();

    }

});

/* =====================================================
   REVIEW STAR RATING
===================================================== */

const starRating = document.querySelector("#starRating");

if (starRating) {

    const stars = starRating.querySelectorAll(
        'input[name="star_rating"]'
    );

    const ratingInput = document.querySelector(
        "#id_rating"
    );


    stars.forEach(function (star) {

        star.addEventListener("change", function () {

            if (ratingInput) {

                ratingInput.value = this.value;

            }

        });

    });

}