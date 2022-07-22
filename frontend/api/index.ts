import APIBase from "./apibase"

let rates = new APIBase("rates")
let assets = new APIBase("assets")
let rateChart = new APIBase("rate-chart")
let sign = new APIBase("users")
let login = new APIBase("token/login")
let account = new APIBase("users/me")

export default {
    rates,
    assets,
    rateChart,
    sign,
    login,
    account
}