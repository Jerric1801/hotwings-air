package com.hotwings.user.dto.points;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class PointsResponse {
    private int loyalty_points;
    private String message;
    private boolean status;
}
