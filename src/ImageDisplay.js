import React from 'react';

function ImageDisplay() {
  return (
    <div>
      <h1>Amazon Prime Data Analysis</h1>
      <iframe
        title="Amazon Prime Data Analysis"
        src="http://localhost:5000/index.html"
        width="100%"
        height="800"
        frameBorder="0"  // To remove iframe border
      ></iframe>
    </div>
  );
}

export default ImageDisplay;
