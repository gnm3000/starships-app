import Image from "next/image";
import Link from "next/link";
export default function Home() {
  return (
    <><h1 className="text-3xl font-bold underline">
      Starshipss
    </h1><p><Link href={"/login"} >Login</Link></p></>

   
  )
}