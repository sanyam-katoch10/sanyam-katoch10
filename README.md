<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sanyam Katoch Portfolio</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap" rel="stylesheet">
<style>
  body {
    margin:0;
    font-family:'Fira Code', monospace;
    background: #0f172a;
    color:#fff;
    overflow-x:hidden;
  }

  /* Wave Neon Background */
  .wave-bg {
    position: absolute;
    width: 200%;
    height: 400px;
    background: linear-gradient(90deg,#8b5cf6,#22d3ee,#facc15,#f43f5e);
    background-size: 400% 400%;
    animation: wave 15s linear infinite;
    top:0; left:-50%;
    filter: blur(120px) opacity(0.35);
    z-index:-1;
  }
  @keyframes wave {
    0%{background-position:0 0;}
    50%{background-position:100% 0;}
    100%{background-position:0 0;}
  }

  /* Glass Card */
  .glass {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(18px);
    border-radius:20px;
    padding:30px;
    margin:20px;
    transition: all 0.3s ease;
  }
  .glass:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow:0 0 40px rgba(168,85,247,0.65);
  }

  /* Snake */
  @keyframes pulse {
    0% { filter: drop-shadow(0 0 15px #A855F7); transform: scale(1); }
    50% { filter: drop-shadow(0 0 40px #A855F7); transform: scale(1.02); }
    100% { filter: drop-shadow(0 0 15px #A855F7); transform: scale(1); }
  }
  @keyframes slither {
    0% { transform: translateX(-120%); }
    100% { transform: translateX(120%); }
  }
  .snake-container{
    overflow:hidden;
    width:100%;
    display:flex;
    justify-content:center;
  }
  .snake {
    width:350px;
    border:4px solid;
    border-image: conic-gradient(#A855F7,#22D3EE,#FACC15,#F43F5E,#A855F7) 1;
    border-radius:20px;
    animation: slither 10s linear infinite, pulse 2s infinite;
    transition: transform 0.3s;
  }
  .snake:hover { transform: scale(1.1); }

  /* Headers */
  h1,h2,h3 { text-align:center; }

  /* Buttons / Demo badges */
  .btn {
    display:inline-block;
    background: linear-gradient(90deg,#8b5cf6,#22d3ee);
    color:#fff;
    padding:10px 20px;
    margin:10px;
    border-radius:10px;
    text-decoration:none;
    font-weight:bold;
    transition:all 0.3s;
  }
  .btn:hover {
    transform:scale(1.05);
    box-shadow:0 0 25px #22d3ee,0 0 50px #8b5cf6;
  }

  /* Section spacing */
  section { padding:80px 20px; }
</style>
</head>
<body>

<div class="wave-bg"></div>

<!-- Hero Section -->
<section>
  <h1>Hi, I'm Sanyam Katoch 👋</h1>
  <p style="text-align:center;">Passionate Developer | ML & Deep Learning | Open Source Contributor</p>
  <div class="snake-container">
    <img class="snake" src="https://raw.githubusercontent.com/sanyam-katoch10/sanyam-katoch10/output/github-snake-neon1.svg" />
  </div>
</section>

<!-- About Section -->
<section>
  <div class="glass">
    <h2>About Me</h2>
    <p>🎓 Building ML-powered & scalable systems<br>
       💼 Actively seeking internships<br>
       🧠 Learning Deep Learning & ML systems<br>
       🤝 Open to Open Source collaboration<br>
       💬 C++ • Python • DSA • Web • ML</p>
  </div>
</section>

<!-- Skills Section -->
<section>
  <div class="glass">
    <h2>Skills</h2>
    <p style="text-align:center;">
      <img src="https://skillicons.dev/icons?i=cpp,c,python,java,git,linux,docker&theme=dark" />
    </p>
  </div>
</section>

<!-- Projects Section -->
<section>
  <div class="glass">
    <h2>Featured Projects</h2>
    <p style="text-align:center;">
      <a class="btn" href="#">ML CAPTCHA Live Demo</a>
      <a class="btn" href="#">Project 2 Demo</a>
      <a class="btn" href="#">Project 3 Demo</a>
    </p>
  </div>
</section>

<!-- Metrics Section -->
<section>
  <div class="glass">
    <h2>Metrics</h2>
    <p style="text-align:center;">
      <img width="48%" src="https://github-readme-stats.vercel.app/api?username=sanyam-katoch10&show_icons=true&theme=transparent&hide_border=true" />
      <img width="48%" src="https://github-readme-streak-stats.herokuapp.com/?user=sanyam-katoch10&theme=transparent&hide_border=true" />
    </p>
    <p style="text-align:center;">
      <img width="45%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=sanyam-katoch10&layout=compact&theme=transparent&hide_border=true" />
    </p>
  </div>
</section>

<!-- Blog Section -->
<section>
  <div class="glass">
    <h2>Latest Writing</h2>
    <p style="text-align:center;">
      <img src="https://github-readme-medium.vercel.app/?username=YOUR_MEDIUM_OR_DEVTO_USERNAME&limit=3&theme=dark" />
    </p>
  </div>
</section>

<!-- Footer -->
<section>
  <p style="text-align:center;">Made with ❤️ by <a href="https://github.com/sanyam-katoch10">Sanyam Katoch</a></p>
</section>

</body>
</html>
