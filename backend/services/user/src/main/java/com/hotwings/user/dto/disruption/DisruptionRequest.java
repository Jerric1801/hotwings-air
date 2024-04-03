package com.hotwings.user.dto.disruption;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class DisruptionRequest {
    private String departure;
    private String flight_number;
}
