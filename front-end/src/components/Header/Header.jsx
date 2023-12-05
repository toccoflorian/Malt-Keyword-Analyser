import reactLogo from '../../assets/react.svg'
import viteLogo from '/vite.svg'
import styles from "./Header.module.scss"

export default function Header() {

    return (<>
        <header className='pos-fixed d-flex br-Gray h80 widthfull'>

            <div className={`d-flex justify-space-e align-center width200 h80 `} >

                <img src={reactLogo} className="logo react fs6" alt="React logo" />
                <img src={viteLogo} className="logo fs6" alt="Vite logo" />
            </div>

            <div className={`d-flex justify-center align-center widthfull`}>
                <h1 className={`${styles} text-center`}>Malt keyword analyser</h1>
            </div>


        </header>
    </>)
}