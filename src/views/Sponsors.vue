<template>
    <div class="col">
        <section class="other" v-if="sponsors.length">
            <div class="other-member" v-for="sponsor in sponsors">
                <img v-bind:src="sponsor.logo" v-bind:alt="sponsor.name" class="people-img"/>
                <span>{{ sponsor.sponsor_organization }}}</span>
                <span class="badge badge-warning">{{ sponsor.sponsor_type }}</span>
                <p>{{ sponsor.about }}</p>
            </div>
        </section>
        <section class="other" v-else>
            <div class="other-member">
                <img src="../assets/images/coming-soon.png" alt="coming-soon" class="people-img"/>
                <span>No Sponsor Yet</span>
                <p>:(</p>
            </div>
            <div class="other-member">
                <img src="../assets/images/coming-soon.png" alt="coming-soon" class="people-img"/>
                <span>No Sponsor Yet</span>
                <p>:(</p>
            </div>
        </section>
    </div>
</template>

<script>
    export default {
        name: 'Sponsors',
        data() {
            return {
                sponsors: [],
            }
        },
        beforeCreate() {
            let sponsors_url = "/api/sponsors/";
            this.$http.get(sponsors_url).then( response => {
                this.sponsors = response.body;
                console.log(this.sponsors);
            });
        },
    }
</script>
