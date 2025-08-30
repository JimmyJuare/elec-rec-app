import { Geist, Geist_Mono, Lexend, Inter } from "next/font/google";
import "../styles/globals.css";

// Load fonts
const lexend = Lexend({ subsets: ["latin"], weight: ["100","200", "300", "400","500","600","700","800","900"] });
const inter = Inter({ subsets: ["latin"], weight: ["100","200", "300", "400","500","600","700","800","900"] });

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.className}>
      <body>
        {children}
      </body>
    </html>
  );
}
