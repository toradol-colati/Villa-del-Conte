with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

target = """.main-nav .container {
  display: flex;
  justify-content: center;
  gap: 300px;
}"""

replacement = """.main-nav .container {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.nav-tabs {
  display: flex;
  justify-content: center;
  gap: 100px;
}
"""

content = content.replace(target, replacement)

append_css = """
/* Language Selector */
.lang-selector {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
}
.lang-select {
  padding: 8px 12px;
  border-radius: 20px;
  border: 1px solid #ddd;
  background-color: #f9f9f9;
  font-family: 'Poppins', sans-serif;
  font-size: 0.9em;
  color: #555;
  cursor: pointer;
  outline: none;
  transition: all 0.3s;
}
.lang-select:hover {
  border-color: #4a9d5f;
}

/* Scroll Animations */
.fade-in-up {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
  will-change: opacity, transform;
}
.fade-in-up.reveal-visible {
  opacity: 1;
  transform: translateY(0);
}

/* Blog Section */
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 40px;
}
.blog-card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.05);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
}
.blog-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}
.blog-image {
  width: 100%;
  height: 200px;
  background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80');
  background-size: cover;
  background-position: center;
}
.blog-card:nth-child(2) .blog-image {
  background-image: url('https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80');
}
.blog-card:nth-child(3) .blog-image {
  background-image: url('https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80');
}
.blog-content {
  padding: 25px;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.blog-content h3 {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.5em;
  color: #4a9d5f;
  margin-bottom: 15px;
}
.blog-content p {
  color: #666;
  font-size: 0.95em;
  line-height: 1.6;
  margin-bottom: 20px;
  flex: 1;
}
.read-more {
  color: #4a9d5f;
  font-weight: bold;
  text-decoration: none;
  font-family: 'Poppins', sans-serif;
  font-size: 0.9em;
  transition: color 0.3s;
}
.read-more:hover {
  color: #3b824e;
}
"""

with open("style.css", "w", encoding="utf-8") as f:
    f.write(content + append_css)

print("Updated style.css")
