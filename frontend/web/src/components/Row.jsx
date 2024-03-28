import Seat from './Seat'

function Row(props) {
    const num_seats = props["num_seats"]
    const details = props["row_details"]
    const seats = []
    let type = 'small'
    if (num_seats === 9) {
        type = 'large'
    }
    for (let i = 0; i < num_seats; i++) {
        seats.push(<Seat key = {i} seat_details={details[i]} type={type}/>)
    }

    return (
        <li className="row row--1">
            <ol className="seats" type="A">
                {seats}
            </ol>
        </li>
    )
}

export default Row