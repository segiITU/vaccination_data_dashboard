import matplotlib.pyplot as plt
import numpy as np
from shared import df
from shiny.express import input, render, ui

ui.page_opts(title="COVID-19 Vaccination Dashboard", fillable=True)

with ui.sidebar():
    ui.input_select(
        "country",
        "Select Country",
        choices=sorted(df['ReportingCountry'].unique())
    )

@render.plot
def vaccination_trend():
    filtered_df = df[df['ReportingCountry'] == input.country()]
    
    plt.figure(figsize=(15, 8))
    
    for vaccine in filtered_df['Vaccine'].unique():
        vaccine_data = filtered_df[filtered_df['Vaccine'] == vaccine]
        bars = plt.bar(vaccine_data['YearWeekISO'], 
                      vaccine_data['NumberOfIndivOneDose'],
                      label=vaccine)
        
        # Add value labels inside bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, height/2,
                    f'{int(height):,}',
                    ha='center', va='center')
    
    plt.yscale('log')
    plt.xticks(rotation=45, ha='right')
    plt.title(f"Vaccination Distribution in {input.country()}")
    
    plt.xlabel("YYYY-MM")
    plt.ylabel("Number of Vaccinated (log scale)")
    plt.legend(title="Vaccine Type")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return plt.gcf()
