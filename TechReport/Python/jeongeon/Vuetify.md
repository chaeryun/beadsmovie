# Vuetify란?

- Vue 기반 **`UI 프레임워크`**
    - **틀**을 갖고 일하는 개념. **빠르고 일관성** 있게, **퀄리티** 있게 만들 수 있다.
    - **생산성**이 높고 일관성이 있어 **유지보수**가 용이하다.
    - **퀄리티** 있게 만들기 쉽고 코드에 대한 **재사용성**이 높다.
- 구글의 **`Material Design`**을 기반으로 설계됨
- Vue에 특화된 UI 프레임워크
- [https://](https://vuetifyjs.com/en/getting-started/installation/)[vuetifyjs.com/en](https://vuetifyjs.com/en/)

# Vuetify 프로젝트 생성

- **Vue CLI**를 통한 프로젝트 생성
    - Vue 개발을 편하게 시작할 수 있도록 **프로젝트를 구성**해주는 도구
    - 초기 프로젝트 구성을 해주어 **폴더 구조, lint, build, webpack 설정에 대한 고민 없이** 프로젝트를 구성할 수 있다.
    - 설치
        
        ```java
        npm install -g @vue/cli
        # OR
        yarn global add @vue/cli
        ```
        
    - 설치 버전 확인
        
        ```java
        vue --version
        ```
        
    - 프로젝트 생성
        
        ```java
        vue create 프로젝트 명
        // Vue CLI 3.0 이상 버전부터 프로젝트를 생성 시 의존 된 라이브러리도 함께 설치됨
        ```
        
    - 프로젝트 실행
        
        ```java
        npm run serve
        //종료 시에는 Ctrl+C
        ```
        
    
- **Vue Router** 설치
    - 클라이언트의 요청 경로에 따라 **해당하는 컴포넌트를 불러와** 페이지를 구성할 수 있다.
    - URL 변경 시 DOM을 새로 갱신하는 것이 아니라 **미리 컴포넌트를 가지고 있다가 변경된 요소 영역만 갱신**한다. (SPA의 특징)
    - 설치
        
        ```java
        npm install vue-router
        ```
        
    - 라우터 속성
        - `String` mode : 기본 값은 Hash 모드 (history 모드를 사용하면 브라우저 히스토리 스택에 기록)
        - `String` redirect : 리다이렉팅 (주로 메인 페이지 등에 사용)
        - `array` routes : 페이지 라우팅 정보
            - `String` path : 페이지 경로 (url)
            - `Object` component : 해당 url 페이지에 사용 할 Component
            - `Array` children : 중첩 라우팅을 위한 배열
    - 라우터 생성
        - `인스턴스 방식으로 생성`
            
            ```java
            //📁router/index.js
            import Vue from 'vue'
            import VueRouter from 'vue-router'
            import Dashboard from '@/views/Dashboard'
            import GridSystem from '@/views/GridSystem'
            
            Vue.use(VueRouter)
            
            const routes = [
                {
                    path: '/',
                    name: 'Dashboard',
                    component: Dashboard
                },
                {
                    path: '/grid-system',
                    name: 'GridSystem',
                    component: GridSystem
                },
            ]
            
            const router = new VueRouter({
                mode: 'history',
                routes
            })
            
            export default router
            ```
            
            ```java
            //📁main.js
            import Vue from 'vue'
            import App from './App.vue'
            import router from './router'
            
            new Vue({
              router,
              render: h => h(App)
            }).$mount('#app')
            ```
            
    - 렌더링
        - 라우터를 생성한 컴포넌트에 `router-view` 태그를 선언하면 URL에 맞게 컴포넌트가 맵핑된다.
            
            ```java
            <template>
            	<div id="app">
            		<router-view/>
            	</div>
            </template>
            ```
            
    - 라우터 링크
        - `<router-link>`는 라우터 지원 앱에서 사용자 네비게이션을 가능하게하는 컴포넌트이다.
        - 목표 위치는 `to` prop로 지정된다.
        - 기본적으로 올바른 `href`를 갖는 `<a>`태그로 렌더링 되지만 `tag` prop로 구성 될 수 있다.
        - `<router-link>`는 다음과 같은 이유로 하드 코드 된 `<a href="...">`보다 선호된다.
            - HTML5 히스토리 모드와 해시 모드에서 모두 동일한 방식으로 작동하므로 모드를 트랜지션하기로 결정하거나 라우터가 IE9에서 해시 모드로 트랜지션 한 경우 변경할 필요가 없다.
            - HTML5 히스토리 모드에서, `router-link`는 클릭 이벤트를 차단하여 브라우저가 페이지를 다시 로드하지 않도록 한다.
            - HTML5 히스토리 모드에서 `base` 옵션을 사용할 때 `to` prop의 URL에 이를 포함 할 필요가 없다.
        - `to` 속성에 동적으로 라우팅 경로를 생성할 수 있다. `v-bind` 속성은 동적 경로를 생성하고 싶을 때 유용하다.
            
            ```java
            <!-- 리터럴 string -->
            <router-link to="home">Home</router-link>
            <!-- 이렇게 렌더링 됩니다. -->
            <a href="home">Home</a>
            
            <!-- `v-bind`를 이용한 표현식 -->
            <router-link v-bind:to="'home'">Home</router-link>
            
            <!-- `v-bind`를 생략하면 다른 prop를 바인딩 하는 것과 같습니다. -->
            <router-link :to="'home'">Home</router-link>
            
            <!-- 위와 같습니다. -->
            <router-link :to="{ path: 'home' }">Home</router-link>
            
            <!-- 이름을 가지는 라우트 -->
            <router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>
            
            <!-- 쿼리가 있으면, `/register?plan=private` 이 됩니다. -->
            <router-link :to="{ path: 'register', query: { plan: 'private' }}">Register</router-link>
            ```
            
    
- **Vuetify** 설치
    - 설치
        
        ```java
        vue add vuetify
        ```
        
    - 설치하면 자동으로 App.vue **기본 레이아웃이 변경**되고 **Vuetify 컴포넌트가 설정**된다. ( + Navigation drawers 추가)
        
        ```java
        //📁App.vue
        <template>
          <v-app>
            <v-app-bar
              app
              color="primary"
              dark
            >
              <div class="d-flex align-center">
                <v-img
                  alt="Vuetify Logo"
                  class="shrink mr-2"
                  contain
                  src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
                  transition="scale-transition"
                  width="40"
                />
        
                <v-img
                  alt="Vuetify Name"
                  class="shrink mt-1 hidden-sm-and-down"
                  contain
                  min-width="100"
                  src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
                  width="100"
                />
              </div>
        
              <v-spacer></v-spacer>
        
              <v-btn
                href="https://github.com/vuetifyjs/vuetify/releases/latest"
                target="_blank"
                text
              >
                <span class="mr-2">Latest Release</span>
                <v-icon>mdi-open-in-new</v-icon>
              </v-btn>
            </v-app-bar>
        
        <v-navigation-drawer app>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="text-h6">
                    Application
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    subtext
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
        
              <v-divider></v-divider>
        
              <v-list
                dense
                nav
              >
                <v-list-item
                  **v-for="item in items"
                  :key="item.title"
                  link
                  :to="item.to"**
                >
                  <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                  </v-list-item-icon>
        
                  <v-list-item-content>
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-navigation-drawer>
        
            <v-main>
              **<router-view/>**
            </v-main>
          </v-app>
        </template>
        
        <script>
        export default {
          name: 'App',
        
          components: {
          },
        
          data: () => ({
            **items: [
              { title: 'Dashboard', icon: 'mdi-view-dashboard', to: '/' },
              { title: 'Grid System', icon: 'mdi-help-box', to: '/grid-system' },
            ],**
            right: null,
          }),
        };
        </script>
        ```
        
    - 설치하면 자동으로 ****main.js에 **plugin이 설치**된다.
        
        ```java
        //📁main.js
        import Vue from 'vue'
        import App from './App.vue'
        import router from './router'
        **import vuetify from './plugins/vuetify'**
        
        Vue.config.productionTip = false
        
        new Vue({
          router,
          **vuetify,**
          render: h => h(App)
        }).$mount('#app')
        ```
