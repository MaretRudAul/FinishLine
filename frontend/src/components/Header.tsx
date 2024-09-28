import React from "react";

interface Header {
  title: string;
  host: string;
  location: string;
  description: string;
  datetime: Date;
  pictureUrl: string;
  tag: string[];
  websiteOrigin: string;
  link: string;
}

const Header = () => {
  return (
    <div className="p-4 text-center bg-black">
      <header className="text-white text-3xl font-bold">Finish Line</header>
    </div>
  );
}


export default Header;
