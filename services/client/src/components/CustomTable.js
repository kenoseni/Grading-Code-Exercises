import React from 'react'
import { Table } from 'react-bootstrap'
import TableHead from './TableHead'
import TableBody from './TableBody'


const CustomTable = (props) => {
    return (
        <Table striped bordered hover variant="dark">
            <TableHead />
            <tbody>
                <TableBody {...props}/> 
            </tbody>

        </Table>
    )
}
export default CustomTable
