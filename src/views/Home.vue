<template>
    <div>
        <section>
            <p class="onelook">
                On One Look
            </p>
            <div class="onlook-items">
                <img src="../assets/images/info.png" alt="info" style="grid-area: img1" class="img1"/>
                <img src="../assets/images/card.png" alt="info" style="grid-area: img2" class="img2"/>
                <img src="../assets/images/calendar.png" alt="info" style="grid-area: img3" class="bottom-items img3"/>
                <img src="../assets/images/video-player.png" alt="info" style="grid-area: img4"
                     class="bottom-items img4"/>
                <span style="grid-area: span1" class="span1">What Is TEDx?</span>
                <span style="grid-area: span2  " class="span2">Be Orator!</span>
                <span style="grid-area: span3" class="bottom-items span3">Scheduling</span>
                <span style="grid-area: span4" class="bottom-items span4">All Videos</span>
                <p style="grid-area: p1" class="p1">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                    eiusmod
                    tempor incididunt ut labore et dolore magna aliqua.</p>
                <p style="grid-area: p2" class="p2">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                    eiusmod
                    tempor incididunt ut labore et dolore magna aliqua.</p>
                <p style="grid-area: p3" class="bottom-items p3">Lorem ipsum dolor sit amet, consectetur adipiscing
                    elit,
                    sed do
                    eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                <p style="grid-area: p4" class="bottom-items p4">Lorem ipsum dolor sit amet, consectetur adipiscing
                    elit,
                    sed do
                    eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            </div>
        </section>
        <div class="dumb-frontend-developer"></div>
        <section class="other" v-if="speakers.length">
            <div class="other-member" v-for="speaker in speakers">
                <img v-bind:src="speaker.picture" v-bind:alt="speaker.name" class="people-img"/>
                <span>{{ speaker.name }}}</span>
                <p>{{ speaker.bio }}</p>
            </div>
        </section>
        <section class="other" v-else>
            <div class="other-member">
                <img src="../assets/images/coming-soon.png" alt="coming-soon" class="people-img"/>
                <span>Mr/Ms Nobody!</span>
                <p>I Said Nobody! :|</p>
            </div>
            <div class="other-member">
                <img src="../assets/images/coming-soon.png" alt="coming-soon" class="people-img"/>
                <span>Mr/Ms Nobody!</span>
                <p>I Said Nobody! :|</p>
            </div>
        </section>
    </div>
</template>

<script>
    export default {
        name: 'Home',
        data() {
            return {
                speakers: [],
            }
        },
        beforeCreate() {
            let speakers_url = "/api/speakers/?status=active";
            this.$http.get(speakers_url).then(response => {
                this.speakers = response.body;
            });
        },
    }
</script>

<style>
    .dumb-frontend-developer {
        height: 10em;
    }
</style>

