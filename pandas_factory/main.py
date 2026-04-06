import pandas as pd

df = pd.read_excel("task_2_data_ex.xlsx")

group_cols = [
    'year',
    'plant_id',
    'produced_material',
    'produced_material_production_type',
    'produced_material_release_type',
    'component_material',
    'component_material_production_type',
    'component_material_release_type'
]

df_group = df.groupby(group_cols, dropna=False).agg({
    'produced_material_quantity': 'sum',
    'component_material_quantity': 'sum'
}).reset_index()

fin_df = df_group[df_group['produced_material_release_type'] == 'FIN']

unique_fin = fin_df[[
    'year',
    'plant_id', 'produced_material',
    'produced_material_production_type',
    'produced_material_release_type',
    'produced_material_quantity'
]].drop_duplicates()

result = []
for _, fin_row in unique_fin.iterrows():
    plant = fin_row['plant_id']
    year = fin_row['year']
    fin_id = fin_row['produced_material']
    fin_rel = fin_row['produced_material_release_type']
    fin_prod = fin_row['produced_material_production_type']
    fin_qty = fin_row['produced_material_quantity']

    queue = [fin_id]
    visited = set()

    while queue:
        cur = queue.pop(0)
        components = df_group[(df_group['produced_material'] == cur) &
                            (df_group['plant_id'] == plant) &
                            (df_group['year'] == year)]
        for _, comp_row in components.iterrows():
            comp_id = comp_row['component_material']
            comp_rel = comp_row['component_material_release_type']

            result.append({
                'plant': plant,
                'fin_material_id': fin_id,
                'fin_material_release_type': fin_rel,
                'fin_material_production_type': fin_prod,
                'fin_production_quantity': fin_qty,
                'prod_material_id': comp_row['produced_material'],
                'prod_material_release_type': comp_row['produced_material_release_type'],
                'prod_material_production_type': comp_row['produced_material_production_type'],
                'prod_material_production_quantity': comp_row['produced_material_quantity'],
                'component_id': comp_row['component_material'],
                'component_material_release_type': comp_row['component_material_release_type'],
                'component_material_production_type': comp_row['component_material_production_type'],
                'component_consumption_quantity': comp_row['component_material_quantity'],
                'year': year
            })

            if comp_rel == 'PROD' and comp_id not in visited:
                queue.append(comp_id)
                visited.add(comp_id)

final_df = pd.DataFrame(result)
cols = ['fin_material_production_type', 'prod_material_production_type', 'component_material_production_type']
for col in cols:
    final_df[col] = final_df[col].astype('Int64')
filename = f"final.xlsx"
final_df.to_excel(filename, index=False)