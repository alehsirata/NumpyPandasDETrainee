WITH RECURSIVE aggregated_bom AS (
    SELECT 
        year, 
        plant_id, 
        produced_material, 
        produced_material_production_type, 
        produced_material_release_type,
        component_material, 
        component_material_production_type, 
        component_material_release_type,
        SUM(REPLACE(REPLACE(REPLACE(produced_material_quantity, ' ', ''), chr(160), ''), ',', '.')::NUMERIC) AS prod_qty, 
        SUM(REPLACE(REPLACE(REPLACE(component_material_quantity, ' ', ''), chr(160), ''), ',', '.')::NUMERIC) AS comp_qty
    FROM task_2_data_ex
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8
),
bom_hierarchy AS (
    SELECT
        plant_id AS plant, 
        produced_material AS fin_material_id,
        produced_material_release_type AS fin_material_release_type,
        produced_material_production_type AS fin_material_production_type,
        prod_qty AS fin_production_quantity, 
        produced_material AS prod_material_id,
        produced_material_release_type AS prod_material_release_type,
        produced_material_production_type AS prod_material_production_type,
        prod_qty AS prod_material_production_quantity, 
        component_material AS component_id,
        component_material_release_type, 
        component_material_production_type,
        comp_qty AS component_consumption_quantity, 
        year
    FROM aggregated_bom
    WHERE produced_material_release_type = 'FIN'

    UNION ALL

    SELECT
        parent.plant, 
        parent.fin_material_id, 
        parent.fin_material_release_type,
        parent.fin_material_production_type, 
        parent.fin_production_quantity,
        child.produced_material AS prod_material_id,
        child.produced_material_release_type AS prod_material_release_type,
        child.produced_material_production_type AS prod_material_production_type,
        child.prod_qty AS prod_material_production_quantity,
        child.component_material AS component_id,
        child.component_material_release_type, 
        child.component_material_production_type,
        child.comp_qty AS component_consumption_quantity, 
        parent.year
    FROM bom_hierarchy parent
    JOIN aggregated_bom child
      ON parent.component_id = child.produced_material
     AND parent.plant = child.plant_id
     AND parent.year = child.year
    WHERE parent.component_material_release_type = 'PROD'
)
SELECT 
    plant, 
    fin_material_id, 
    fin_material_release_type, 
    fin_material_production_type, 
    fin_production_quantity, 
    prod_material_id, 
    prod_material_release_type, 
    prod_material_production_type, 
    prod_material_production_quantity, 
    component_id, 
    component_material_release_type, 
    component_material_production_type, 
    component_consumption_quantity, 
    year
FROM bom_hierarchy;
