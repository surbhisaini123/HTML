
let express=require('express')
let mongoose=require('mongoose')
let upload =require('./Upload')

let bcrypt=require('bcrypt')
let User =require('./User')
let jwt=require('jsonwebtoken')
// const cors = require("./cors");

mongoose.connect("mongodb://127.0.0.1:27017/insta").then(()=>{
    console.log("db...........");
})
let cors=require('cors');
// const User = require('./user');

let app=     express()
app.use(cors())
   app.use(express.json())
  app.get('/', (req,res) =>{
    res.send("hello");
})
//  -----------SINGUP ---
// app.post("/signup,",async(req,res)=>{
//     try{ 
//         const{name,email,passWord}=req.body;
//         const existingUser=await User.findOne({email})
//         if (existingUser)
//             return res.status(400).json({msg:"already  exist"})
//         const hashedPassword=await bcrypt.hash(passWord,10)
//         const newUser=new User ({name,email,passWord,hashedPassword})
//         await newUser.save();
//         res.json({msg:"singup succesful",user:newUser})
 
//     }catch(err){
//         return res.status(500).json({msg:"error during signuo",error:err.message})
//     }
// });

// app.use(express.json());
app.post("/signup", async (req, res) => {
    try {
      const { name, email, passWord } = req.body;
      const existingUser = await User.findOne({ email });
      if (existingUser) return res.status(400).json({ msg: "User already exists" });
  
      const hashedPassword = await bcrypt.hash(passWord, 10);
      const newUser = new User({ name, email, passWord: hashedPassword });
      await newUser.save();
  
      res.json({ msg: "Signup successful", user: newUser });
    } catch (err) {
     return  res.status(500).json({ msg: "Error during signup", error: err.message });
    }
  });



// -------login ------

// app.post("/login",async(req,res)=>{
//     try{
//         const{email,passWord}=req.body
//         const User =await User.findOne({email})
//         console.log(User,"user");
        
//         if(!User)
//             return res.status(400).json({msg:"user not found"})
//         console.log("plain password:",passWord);
//         console.log("hashed from db:",User.passWord);

//         const isMatch=await bcrypt.compare(passWord,User.passWord)
//         if(!isMatch)
//             return res.status(401).json({msg:"invalid credentials"})

//         const token =jwt.sign({
//             _id:User._id,email:User.email,role:User.role||"user"},
//             "SECRETE123",

//         );
//         res.json({
//             mag:"login successful",
//             token,
//             User:{_id:User._id,name:User.name,email:User.email}
//         });
//     }catch(err){
//         return res.status(500).json({msg:"error during login",error:err.message});

//     }
    
// });

  app.post("/login", async (req, res) => {
    try {
      const { email, passWord } = req.body;
      const user = await User.findOne({ email });
      console.log(user ,"user");
      if (!user) return res.status(404).json({ msg: "User not found" });
  
      console.log("Plain Password:", passWord);
  console.log("Hashed from DB:", user.passWord);
  
      const isMatch = await bcrypt.compare(passWord, user.passWord);
      if (!isMatch) return res.status(401).json({ msg: "Invalid credentials" });
  
     const token = jwt.sign(
    { _id: user._id, email: user.email, role: user.role || "user" },
    "SECRET123",
    { expiresIn: "1h" }
  );
  
  
  res.json({
    msg: "Login successful",
    token,
    user: { _id: user._id, name: user.name, email: user.email }
  });
    } catch (err) {
     return res.status(500).json({ msg: "Error during login", error: err.message });
    }

})


// middleware/auth.js


let auth = function(req, res, next) {
    const token = req.headers.authorization;
    console.log("header",req.headers)
    // console.log("hello",token);
    if (!token) return res.status(401).json({ message: "Login first!" });

    try {
        const decoded = jwt.verify(token, "SECRET123");
        console.log(decoded,"kyaya ");
        
        req.user = decoded;   // IMPORTANT: req.user yahi se aata hai
        console.log("decoded",decoded);
        next();
    } catch (err) {
        return res.status(401).json({ message: "Invalid token" });
    }
};

app.post('/upload',async(req,res)=>{
    let {imgUrl} =req.body;
    if(!imgUrl){
        return res.send("not found url")

    }
    let uploaD=new Upload({
        imgUrl,
           user:userId,
           likedBy:[],
    });
    await uploaD.save()
    return res.send("upload urll")

})




app.post("/follow:id",async(req,res)=>{
    let targetUserId=req.params.id
    let currentUserId=req.user.id
    if(targetUserId==currentUserId){
        res.json({msg:"same to n h"})
    }
    let targetUser=await User.findById(targetUserId)
    let currentUser=await User.findById(currentUserId)
    if(!currentUser||!targetUser){
        res.send("user not found")
    }

    //unfollow
    let alreadyFollow=currentUser.following.includes(targetUserId)
    if(alreadyFollow){
        currentUser.following=currentUser.following.filter((id)=>{
            return id!=targetUserId
        })
        targetUser.followers=targetUser.followers.filter((id)=>{
            return id!=currentUserId
        })
       await currentUser.save()
       await targetUser.save()
       res.json("unfollowww")
    }

    //-----follow-------
    currentUser.following.push(targetUserId)
    targetUser.followers.push(currentUserId)
    await currentUser.save()
    await targetUser.save()
    res.json({msg:"follow succes"})
})

app.post("/search", async(req,res)=>{
    let query =req.query.q
    if(!query){
        return res.send("query is not found")
    }
    let isMatch=await User.find({
        $or:[
            {name:{$regex:query,$options:"i"}},
            {email:{$regex:query,$options:"i"}},
        ]

    }).limit(1)
    res.json({msg:isMatch})

})





app.listen(4000,()=>{
    console.log("server running on port no. 4000");
    
})

