import React from 'react';
import ImageDisplay from './ImageDisplay';

function App() {
  return (
    <div className="App">
      <ImageDisplay/>
    </div>
  );
}

export default App;























// import React, { useEffect, useState } from 'react';

// function App() {
//   const [plotUrl, setPlotUrl] = useState(null);

//   useEffect(() => {
//     // Make an API request to fetch the plot image
//     fetch('/plot')  // Use a relative path to the Flask endpoint
//       .then((response) => response.blob())
//       .then((blob) => {
//         const url = URL.createObjectURL(blob);
//         console.log('Image URL:',url);
//         setPlotUrl(url);
//       });
//   }, []);

//   return (
//     <div className="App">          
//       {/* {plotUrl && <img src={"http://localhost:5000/plot"} alt="Plot" />} */}
     
//       {plotUrl && <img src={"http://localhost:5000/plot3"} alt="Plot3" />}
//     </div>

    
//   );

    
// }

// export default App;





