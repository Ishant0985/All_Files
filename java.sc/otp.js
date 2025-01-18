function OTP(){
    let OTP =""
    otp = math.floor(math.random()*9000+1000)
    return otp
}
console.log("Your OTP is",OTP)