
## request.user是django权限验证系统的基础
### 登录和AuthenticationMiddleware都基于AUTHENTICATION_BACKENDS认证用户信息
> AUTHENTICATION_BACKENDS = [django.contrib.auth.backends.ModelBackend]
#### 登录流程
> admin.site.urls
> admin.site.login()
>> LoginView(AdminAuthenticationForm -> AuthenticationForm) 
>>> AuthenticationForm() -> errors 初始化,供form.is_valid()使用
>>>> AuthenticationForm.is_valid()  ->  form.errors -> form.full_clearn -> form._clean_form -> form.clean
>>>> AuthenticationForm.clean() -> user{绑定在form} = auth.authenticate -> ModelBackend[AUTHENTICATION_BACKENDS].authenticate(数据库验证用户名密码)  # 认证
>>> LoginView.form_valid() -> auth.login(AuthenticationForm.user)  # seesion绑定用户ID, 认证的uer绑定到request.user， 分发消息
```
https://www.jianshu.com/p/9bcd67b4b2d1

LoginView <- auth.views.LoginView
AuthenticationForm <- auth.forms.AuthenticationForm
```

#### AuthenticationMiddleware
> 常规请求流程中解决request.user的赋值
```
AuthenticationMiddleware
1.通过session获取到用户ID
2.通过AUTHENTICATION_BACKENDS基于用户ID，获取用户数据

```

