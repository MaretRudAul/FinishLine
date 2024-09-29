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
    <div className="p-4 text-center bg-white">
      <header className="text-black text-3xl font-bold font-sans italic tracking-normal">Finish Line</header>
    </div>
  );
}


export default Header;
