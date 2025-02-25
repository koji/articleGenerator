import { useState } from 'react';
import { BlogDisplay, BlogForm, LoadingIndicator, ErrorMessage } from './components'; // Assume this component exists
import './App.css';

function App() {
  const [blogPost, setBlogPost] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleGenerateBlog = async (topic: string) => {
    setLoading(true);
    setError(null);
    setBlogPost(null);
    try {
      const response = await fetch('http://localhost:8000/generate-blog', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic }),
      });
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to generate blog post');
      }
      const data = await response.json();
      setBlogPost(data.blog_post);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Article Generator</h1>
      <BlogForm onSubmit={handleGenerateBlog} />
      {loading && <LoadingIndicator />}
      {error && <ErrorMessage message={error} />}
      {blogPost && <BlogDisplay content={blogPost} />}
    </div>
  );
}

export default App;
