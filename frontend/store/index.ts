import { createStore } from 'vuex'

export interface MyState{
    collapse: boolean, 
    // access: string,
    refresh: string,
    user: {},
    isAuthenticated: boolean,
    token: string
}

//-------------------------- JWT ----------------------------//

// const store = createStore<MyState>(
//     {
//         state:{
//             collapse: false,
//             access: '',
//             refresh: '',
//             isAuthenticated: false,
//             user: {
//                 id:0,
//                 username:'',
//             },
//         },
//         mutations:{
//             initializeStore(state){
//                 if (localStorage.getItem("access")){
//                     state.access = localStorage.getItem("access")
//                     state.isAuthenticated = true
//                     state.user.username = localStorage.getItem('username')
//                     state.user.id = localStorage.getItem('userid')
//                 } else {
//                     state.access = ''
//                     state.isAuthenticated = false
//                     state.user.id = 0
//                     state.user.username = ''
//                 }
//             },
//             setAccess(state, access){
//                 state.access = access
//                 state.isAuthenticated = true
//             },
//             setUser(state, user){
//                 state.user = user
//               },
//             setCollapse(state: MyState, collapse:boolean){
//                 state.collapse = collapse
//             }
//         },
//         getters:{
//             getCollapse(state:MyState){
//                 return state.collapse
//             },
//             getUserinfo(state:MyState){
//                 return state.user
//             },
//             getAccess(state:MyState){
//                 return state.access
//             },
//         }

//     }
// )

const store = createStore<MyState>(
    {
        state:{
            collapse: false,
            token: '',
            refresh: '',
            isAuthenticated: false,
            user: {
                id:0,
                username:'',
            },
        },
        mutations:{
            initializeStore(state){
                if (localStorage.getItem("token")){
                    state.token = localStorage.getItem("token")
                    state.isAuthenticated = true
                    state.user.username = localStorage.getItem('username')
                    state.user.id = localStorage.getItem('userid')
                } else {
                    state.token = ''
                    state.isAuthenticated = false
                    state.user.id = 0
                    state.user.username = ''
                }
            },
            setToken(state, token){
                state.token = token
                state.isAuthenticated = true
            },
            removeToken(state){
                state.token = ''
                state.isAuthenticated = false
              },
            setUser(state, user){
                state.user = user
              },
            setCollapse(state: MyState, collapse:boolean){
                state.collapse = collapse
            }
        },
        getters:{
            getCollapse(state:MyState){
                return state.collapse
            },
            getUserinfo(state:MyState){
                return state.user
            },
            getToken(state:MyState){
                return state.token
            },
        }

    }
)

export default store