var app = new Vue({
    el: '#vue-outer',
    data: {
        loading: false,
        login_info: { email: null, password: null },
        error: ''
    },
    computed: {},

    mounted: function () {

    },

    methods: {
        login: function () {
            var self = this;
            this.loading = true;

            let info = self.login_info;
            let payload = {
                email: info.email,
                password: info.password
            };

            fetch('/login', {
                method: 'POST',
                body: JSON.stringify(payload),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(
                function (res) {
                    if (res.status == 200) {
                        res.json().then(function (data) {
                            localStorage.setItem('token', data['token']);
                            window.location.href = '/';
                        });
                    } else {
                        //Throw error
                        alert('Invalid email or password!');
                    }
                }
            ).catch(
                function (err) {
                    console.error(err);
                    alert('Invalid request!');
                }
            );
        }
    }
});
