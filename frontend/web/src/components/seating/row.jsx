import Seat from './seat'

function Row(props) {

    return (
        <li class="row row--1">
            <ol class="seats" type="A">
                <Seat/>
                <Seat/>
                <Seat/>
                <Seat/>
                <Seat/>
                <Seat/>
            </ol>
        </li>
    )
}

export default Row