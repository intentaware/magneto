describe('Login Test', function() {
  var username = element(by.id('id_username'));
  var password = element(by.id('id_password'));
  var form  = element(by.name('loginForm'));

  beforeEach(function() {
    browser.get('http://127.0.0.1:8000/users/auth/login/');
  });

  it('State 200 Check', function(){
    expect(browser.getTitle()).toEqual('IntentAware | Login');
  });

  it('Populate n Submit', function(){
    username.sendKeys('alphanum@yahoo.com');
    password.sendKeys('alpha101');

    form.submit();


  });
});
