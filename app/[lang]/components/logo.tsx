import Image from "next/image";

export default function Logo() {
    return (
        <div>
            <Image
                src="next.svg"
                alt="data-tool logo"
                width={100}
                height={100}
            />
        </div>
    )
}