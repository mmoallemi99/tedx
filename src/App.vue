<template>
    <div>
        <nav class="mobile_nav">
            <ul class="mobile_nav_ul">
                <li>
                    <img alt="Home" src="./assets/images/home.svg" class="mobile_nav_img">
                    <router-link to="/" v-on:click.native="close_nav">Home</router-link>
                </li>
                <li>
                    <img alt="Team" src="./assets/images/team.svg" class="mobile_nav_img">
                    <router-link to="/team" v-on:click.native="close_nav">Team</router-link>
                </li>
                <li>
                    <img alt="Sponsors" src="./assets/images/sponsor.svg" class="mobile_nav_img">
                    <router-link to="/sponsors" v-on:click.native="close_nav">Sponsors</router-link>
                </li>
                <li>
                    <img alt="Nominate" src="./assets/images/nominate.svg" class="mobile_nav_img">
                    <router-link to="/nominate" v-on:click.native="close_nav">Nominate</router-link>
                </li>
                <li id="close_nav" v-on:click="close_nav"> Close</li>
            </ul>
        </nav>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <header class="header">
                        <router-link to="/">
                            <img src="./assets/images/logo.png" alt="LOGO" class="logo"/>
                        </router-link>
                        <div class="hamburger-nav">
                            <label for="toggle">&#9776;</label>
                            <input type="checkbox" id="toggle" v-on:click="open_nav"/><br/>
                            <nav class="main_nav">
                                <ul>
                                    <div id="item-1"></div>
                                    <li v-for="link in links">
                                        <router-link v-bind:to="link.url" v-on:click.native="change_current_nav_location">{{ link.name }}</router-link>
                                    </li>
                                </ul>
                            </nav>
                        </div>
                    </header>
                    <div class="row">
                    <router-view/>
                    </div>
                    <footer>
                        <p class="copyright"> Copyright ©2019 All rights reserved |
                            Reza Hasani
                            &
                            <a style="color: mediumseagreen; text-decoration: none;" href="https://www.linkedin.com/in/mmoallemi99/"
                               target="_blank">Mohammad
                                Moallemi</a>
                        </p>
                        <div class="social-networks">
                            <a href="#">
                                <img src="./assets/images/facebook.png" alt="Facebook"/>
                            </a>
                            <a href="#">
                                <img src="./assets/images/google-plus.png" alt="Google+"/>
                            </a>
                            <a href="#">
                                <img src="./assets/images/instagram.png" alt="Instagram"/>
                            </a>
                            <a href="#">
                                <img src="./assets/images/twitter.png" alt="Twitter"/>
                            </a>
                            <a href="#">
                                <img src="./assets/images/telegram.png" alt="Telegram"/>
                            </a>
                        </div>
                    </footer>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        assetsPublicPath: '/asdsad/',
        name: "App",
        data() {
            return {
                links: [
                    {url: "/", name: "Home",},
                    {url: "/team", name: "Team",},
                    {url: "/sponsors", name: "Sponsors",},
                    {url: "/nominate", name: "Nominate",},
                ],
                pathname: this.$route.name,
                mobile_nav_open: false,
            }
        },
        methods: {
            change_current_nav_location() {
                this.pathname = this.$route.name;
                let pathname = this.pathname;
                let navbar = $('.main_nav ul li');
                let current_tab = $('#item-1');
                let tabs_count = navbar.length;
                let tab_width = navbar.css('width');
                tab_width = tab_width.replace(/[^-\d\.]/g, '');
                for (let i = 0; i < tabs_count; i++) {
                    let li_value = navbar.eq(i).text().trim().toLowerCase();
                    if (pathname.indexOf(li_value) !== -1) {
                        let left = (40 + i * tab_width) + 'px';
                        current_tab.css({'left': left, 'transition': 'none', 'display': 'block'});
                    } else if (pathname === '/') {
                        current_tab.css({'left': '40px', 'transition': 'none', 'display': 'block'});
                    }
                }
                let current_tab_location = current_tab.css('left');
                for (let i = 0; i < tabs_count; i++) {
                    navbar.eq(i).hover(function () {
                        let left = (40 + i * tab_width) + 'px';
                        current_tab.css({'left': left, 'transition': 'left 300ms'});
                    });
                    navbar.eq(i).mouseleave(function () {
                        current_tab.css({'left': current_tab_location, 'transition': 'left 300ms'});
                    });
                }
            },
            open_nav() {
                $(function () {
                    let mobile_nav = $('.mobile_nav');
                    let body = $('.flip-card');
                    let inside_body = $('.flip-card-inner');
                    body.css('transform', 'rotateY(45deg)');
                    inside_body.css({
                        'transform': 'rotateY(45deg)',
                        'left': '-25%',
                    });
                    mobile_nav.show();
                    mobile_nav.animate({
                        'width': '44%',
                    }, 1);
                });
            },
            close_nav() {
                $(function () {
                    let mobile_nav = $('.mobile_nav');
                    let body = $('.flip-card');
                    let inside_body = $('.flip-card-inner');
                    body.css('transform', 'rotateY(0deg)');
                    inside_body.css({
                        'transform': 'rotateY(0deg)',
                        'left': '0',
                    });
                    mobile_nav.animate({
                        'width': '0',
                    }, 1);
                    mobile_nav.hide();
                });
            },
        },
        created() {
            let pathname = this.pathname;
            $(function () {
                // DOM Cache
                let navbar = $('.main_nav ul li');
                let current_tab = $('#item-1');
                let tabs_count = navbar.length;
                let tab_width = navbar.css('width');
                tab_width = tab_width.replace(/[^-\d\.]/g, '');
                $(window).on('resize', function () {
                    tab_width = navbar.css('width');
                    tab_width = tab_width.replace(/[^-\d\.]/g, '');
                });

                // Nav
                for (let i = 0; i < tabs_count; i++) {
                    let li_value = navbar.eq(i).text().trim().toLowerCase();
                    if (pathname.indexOf(li_value) !== -1) {
                        let left = (40 + i * tab_width) + 'px';
                        current_tab.css({'left': left, 'transition': 'none', 'display': 'block'});
                    } else if (pathname === '/') {
                        current_tab.css({'left': '40px', 'transition': 'none', 'display': 'block'});
                    }
                }
                let current_tab_location = current_tab.css('left');
                for (let i = 0; i < tabs_count; i++) {
                    navbar.eq(i).hover(function () {
                        let left = (40 + i * tab_width) + 'px';
                        current_tab.css({'left': left, 'transition': 'left 300ms'});
                    });
                    navbar.eq(i).mouseleave(function () {
                        current_tab.css({'left': current_tab_location, 'transition': 'left 300ms'});
                    });
                }
            });
        }
    }
</script>

<style>

</style>
