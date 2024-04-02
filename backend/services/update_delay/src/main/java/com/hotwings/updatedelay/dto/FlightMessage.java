package com.hotwings.updatedelay.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class FlightMessage {
    private String flight_id;
    private String date;
    private String flight_number;
}
