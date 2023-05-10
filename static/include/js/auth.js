var app = new Vue({
    el: '#vue-outer',
    data: {
        loading: false,
        login_info: { email: null, password: null },
        error: ''
    },
    computed: {},
    beforeCreate: function () {
        let token = localStorage.getItem('token');
        if (token) {
            fetch('/validate', {
                method: 'POST',
                body: JSON.stringify({ token: token }),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(
                function (res) {
                    if (res.status == 200) {
                        //token found and validated
                        window.location.href = '/';
                    } else {
                        localStorage.removeItem('token');
                    }
                }
            ).catch(
                function (err) {
                    localStorage.removeItem('token');
                }
            );

        } else {
            localStorage.removeItem('token');
        }
    },
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
