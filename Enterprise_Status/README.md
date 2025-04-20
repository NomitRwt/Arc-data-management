Requirements:

1. Need to set up environment variables for username and password
2. Need to edit the serivce and the portal url's to check

Here's a simple analogy to help you understand **token-based authentication**:

---

### 🧁 **The Bakery Analogy**

Imagine you go to a bakery that has a **VIP lounge** where you can enjoy free pastries, but only **registered customers** are allowed inside.

---

### 🧍‍♂️ Step 1: **Login (Proving who you are)**  
You walk up to the counter and show your **membership card** (username + password).  
The bakery checks your ID and confirms: "Yes, you're a member!"

---

### 🪪 Step 2: **Token Issuance (Getting a pass)**  
Instead of asking for your ID every time you want a pastry, the bakery gives you a **VIP pass** (a token).  
This pass doesn't contain your name, but it contains a **secret code** that proves it's legit.

---

### 🍩 Step 3: **Accessing services**  
Now, whenever you want pastries, you just show your **VIP pass**.  
As long as the pass is **valid and untampered**, the bakery lets you in — no need to show ID again!

---

### ⏳ Step 4: **Expiration**  
Your VIP pass expires in 1 hour. After that, you’ll need to log in again and get a **new pass**.

---

### 🚫 Step 5: **Security**  
If someone steals your VIP pass, they can use it unless:
- It’s expired  
- You or the bakery **revoke** it  
- The pass is **encrypted**, making it hard to fake or modify

---

### 🧠 In Tech Terms:
- Login = providing credentials  
- Token = a signed piece of data proving you're authenticated (like JWT)  
- Token is stored (in browser/app) and sent with every request  
- Server **verifies** the token and gives access

---

Article on [token based authentication](https://www.geeksforgeeks.org/how-does-the-token-based-authentication-work/)
