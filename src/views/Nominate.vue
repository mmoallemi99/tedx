<template>
    <div class="col">
        <section>
            <div class="register-field-lg">
                <div class="register-field-sm">
                    <img src="../assets/images/picture.png" alt="Beta"/>
                    <form id="nomination-form" v-on:submit.prevent="submitForm" method="POST">

                        <input v-model="newSpeaker.first_name" type="text" name="first_name" class="nomination-input"
                               placeholder="First Name"
                               maxlength="30" required id="id_first_name">

                        <input v-model="newSpeaker.last_name" type="text" name="last_name" class="nomination-input"
                               placeholder="Last Name"
                               maxlength="30" required id="id_last_name">


                        <input v-model="newSpeaker.email" type="email" name="email" class="nomination-input"
                               placeholder="Email" required
                               id="id_email">


                        <input v-model="newSpeaker.phone_number" type="tel" name="phone_number" class="nomination-input"
                               placeholder="Phone Number"
                               required id="id_phone_number">


                        <textarea v-model="newSpeaker.bio" placeholder="Please Describe Yourself..." name="biography"
                                  cols="40" rows="10" maxlength="500"
                                  required id="id_biography">

</textarea>

                        <input type="submit" value="SUBMIT"/>
                        <div v-html="formMessage" id="results" v-bind:class="{
                                                            alert: formMessage.length,
                                                            'alert-gold': formSuccess,
                                                            'alert-error': formError,
                                                        }
                        ">
                        </div>
                    </form>
                </div>
            </div>
        </section>
    </div>
</template>

<script>

    export default {
        name: 'Nominate',
        data() {
            return {
                newSpeaker: {
                    "first_name": "",
                    "last_name": "",
                    "email": "",
                    "phone_number": "",
                    "bio": "",
                },
                formMessage: '',
                formSuccess: false,
                formError: false,
            }
        },
        methods: {
            successCallback(response) {
                this.formError = false;
                this.formSuccess = true;
                this.formMessage = `Form Submitted Successfully! We Will Contact You ASAP`;
                return true;
            },
            errorCallback(response) {
                let errors = response.body;
                let errString = '';
                for (let key in errors) {
                    errString += `Error in Field ${key}: ${errors[key]}<br>`;
                }
                this.formMessage = errString;
                this.formError = true;
                this.formSuccess = false;
                return false;
            },
            submitForm() {
                let speakers_url = "/api/speakers/";
                // let csrftoken = this.getCookie('csrftoken');
                // console.log(csrftoken);
                this.$http.post(speakers_url, this.newSpeaker).then(this.successCallback, this.errorCallback);
                // console.log(csrftoken);
            },
            // getCookie(name) {
            //     let cookieValue = null;
            //     if (document.cookie && document.cookie !== '') {
            //         let cookies = document.cookie.split(';');
            //         for (let i = 0; i < cookies.length; i++) {
            //             let cookie = cookies[i].trim();
            //             Does this cookie string begin with the name we want?
            // if (cookie.substring(0, name.length + 1) === (name + '=')) {
            //     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            //     break;
            // }
            // }
            // }
            // return cookieValue;
            // }
        },
        // created() {
        //     let csrftoken = this.getCookie('csrftoken');
        //     console.log(csrftoken);
        // }
    }
</script>
