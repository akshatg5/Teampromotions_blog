// Define the URL for fetching data from Sanity
const PROJECT_ID = "t1vue1v5"; // Replace with your Sanity project ID
const DATASET = "production"; // Replace with your dataset name
const QUERY = encodeURIComponent('*[_type == "blog"]'); // Adjust the type according to your Sanity schema
const URL = `https://${PROJECT_ID}.api.sanity.io/v1/data/query/${DATASET}?query=${QUERY}`;

// Function to create a blog post element
function createBlogPost(blogPost) {
    const article = document.createElement("article");
    article.className = "hentry post post-standard has-post-thumbnail sticky";
  
    article.innerHTML = `
      <div class="post-thumb">
        <img loading="lazy" src="${blogPost.featuredImage?.url || ''}" alt="${blogPost.title}">
        <!-- ... Rest of the code ... -->
      </div>
      <!-- ... Rest of the code ... -->
    `;
  
    return article;
  }
  

// Fetch the content from Sanity
fetch(URL)
  .then((res) => res.json())
  .then((data) => {
    if (data.result) {
      const blogPosts = data.result;

      // Assuming you have a container div with the class "blog-posts-container"
      const container = document.querySelector(".blog-posts-container");

      blogPosts.forEach((blogPost) => {
        const article = createBlogPost(blogPost);
        container.appendChild(article);
      });
    }
  })
  .catch((err) => console.error(err));
