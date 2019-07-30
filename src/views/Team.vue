<template>
        <section v-if="staff.length" class="people">
            <div class="people-member" v-for="member in staff">
                <img v-bind:src="member.picture" v-bind:alt="member.name" class="people-img"/>
                <span>{{ member.name }}</span>
                <span class="badge badge-warning">{{ member.role }}</span>
                <p>{{ member.bio }}</p>
                <!--                <div v-if="false" class="people-member-social">-->
                <!--                    {% else %}-->
                <!--                    <div>-->
                <!--                        {% endif %}-->
                <!--                        {% if x.github_account %}-->
                <!--                        <a href="https://www.github.com/{{ x.github_account }}" target="_blank">-->
                <!--                            <div class="member-social">-->
                <!--                                <img alt="github_account" src="{% static 'images/github-icon.png' %}">-->
                <!--                            </div>-->
                <!--                        </a>-->
                <!--                        {% endif %}-->
                <!--                        {% if x.linkedin_account %}-->
                <!--                        <a href="https://www.linkedin.com/in/{{ x.linkedin_account }}" target="_blank">-->
                <!--                            <div class="member-social">-->
                <!--                                <img alt="linkedin_account" src="{% static 'images/linkedin-icon.png' %}">-->
                <!--                            </div>-->
                <!--                        </a>-->
                <!--                        {% endif %}-->
                <!--                    </div>-->
                <!--                </div>-->

            </div>
        </section>
        <section class="other" v-else-if="staff.length === 0">
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
</template>

<script>
    export default {
        name: 'Team',
        data() {
            return {
                staff: [],
            }
        },
        beforeCreate() {
            let staff_url = "/api/staffs/";
            this.$http.get(staff_url).then(response => {
                this.staff = response.body;
            });
        },
    }
</script>
